from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.db import forms_collection
from app.models import FormData, get_field_type


app = FastAPI()




@app.post('/get_form')
def process_form(data: FormData):
    fields = {field: value for field, value in data.dict().items() if field.startswith("f_")}
    
    forms = forms_collection.find()
    
    matching_form = None
    for form in forms:
        template_fields = {field['name']: field['type'] for field in form['fields']}
        if set(fields.keys()).issubset(set(template_fields.keys())):
            matching_form = form
            break
    
    if matching_form:
        return {'template_name': matching_form['name']}
    else:
        field_types = {}
        for field, value in fields.items():
            field_type = get_field_type(value)
            if field_type:
                field_types[field] = field_type
            else:
                field_types[field] = "FIELD_TYPE"
        
        return field_types
