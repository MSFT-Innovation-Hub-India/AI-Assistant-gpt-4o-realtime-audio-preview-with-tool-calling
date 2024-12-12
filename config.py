#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os
from dotenv import load_dotenv
load_dotenv()

class DefaultConfig:
    """ Bot Configuration """

    az_openai_key=os.getenv("az_openai_key")
    az_openai_baseurl=os.getenv("az_openai_baseurl")
    az_open_ai_endpoint_name=os.getenv("az_open_ai_endpoint_name")
    az_openai_type=os.getenv("az_openai_type")
    az_openai_api_version=os.getenv("az_openai_api_version")
    deployment_name=os.getenv("deployment_name")

    attlassian_api_key=os.getenv("attlassian_api_key")
    attlassian_user_name=os.getenv("attlassian_user_name")
    attlassian_url=os.getenv("attlassian_url")
    
    ai_search_url=os.getenv("ai_search_url")
    ai_search_key=os.getenv("ai_search_key")
    ai_index_name=os.getenv("ai_index_name")
    ai_semantic_config=os.getenv("ai_semantic_config")

    # The following is for the demo to Gameskraft
    grievance_project_key=os.getenv("grievance_project_key")
    grievance_type=os.getenv("grievance_type")
    grievance_project_name=os.getenv("grievance_project_name")


    ai_assistant_organization_name = "Contoso Gaming Inc."


    az_db_server=os.getenv("az_db_server")
    az_db_database=os.getenv("az_db_database")
    az_db_username=os.getenv("az_db_username")
    az_db_password=os.getenv("az_db_password")
