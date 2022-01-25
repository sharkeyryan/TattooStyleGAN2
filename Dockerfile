# Copyright (c) 2019, NVIDIA Corporation. All rights reserved.
#
# This work is made available under the Nvidia Source Code License-NC.
# To view a copy of this license, visit
# https://nvlabs.github.io/stylegan2/license.html

FROM tensorflow/tensorflow:1.15.0-gpu-py3

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

WORKDIR /app

RUN mkdir -p /app/raw-images
RUN mkdir -p /app/datasets
RUN mkdir -p /app/result-sets

RUN pip install scipy==1.3.3
RUN pip install requests==2.22.0
RUN pip install Pillow==6.2.1
RUN pip install opencv-python