#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from .config import current_config

app = Flask(__name__,
            template_folder="../templates",
            static_folder="../static")
app.config.from_object(current_config)

from .db import *
from .api import *
