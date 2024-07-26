import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from pathlib import Path
from cnnClassifier.entity.config_entity import (ModelTrainerConfig)


class ModelTraining:
  def __init__(self, config: ModelTrainerConfig):
    self.config = config

  def get_base_model(self):
    self.model = tf.keras.models.load_model(
      self.config.updated_base_model_path
    )

  def train_valid_generator(self):
    datagenerator_kwargs = dict(
      rescale=1./255,
      validation_split=0.2
    )

    dataflow_kwargs = dict(
      target_size=self.config.params_image_size[:-1],
      batch_size=self.config.params_batch_size,
      interpolation='bilinear'
    )

    valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
      **datagenerator_kwargs
    )

    self.valid_datagenerator = valid_datagenerator.flow_from_directory(
      directory=self.config.training_data,
      subset='validation',
      shuffle=False,
      **dataflow_kwargs
    )

    if self.config.params_is_augmentation:
      train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        **datagenerator_kwargs
      )
    else:
      train_datagenerator = valid_datagenerator

    self.train_datagenerator = train_datagenerator.flow_from_directory(
      directory=self.config.training_data,
      subset='training',
      shuffle=True,
      **dataflow_kwargs
    )


  @staticmethod
  def save_model(path: Path, model: tf.keras.Model):
    model.save(path)


  def train(self):
    self.steps_per_epoch = self.train_datagenerator.samples // self.train_datagenerator.batch_size
    self.validation_steps = self.valid_datagenerator.samples // self.valid_datagenerator.batch_size

    self.model.fit(
      self.train_datagenerator,
      epochs=self.config.params_epochs,
      steps_per_epoch=self.steps_per_epoch,
      validation_data=self.valid_datagenerator,
      validation_steps=self.validation_steps
    )

    self.save_model(path=self.config.trained_model_path, model=self.model)