#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from local_config import LocalConfig
    current_config = LocalConfig
except:
    from config import Config
    current_config = Config
