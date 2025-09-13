import json

import weave
from openai import OpenAI

import config
from utils import fn_to_schema, tag

weave.init(project_name=config.WEAVE_PROJECT)

class MiniAgent(weave.Model)

    client: OpenAI = None
