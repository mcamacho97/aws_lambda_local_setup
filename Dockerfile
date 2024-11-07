FROM public.ecr.aws/lambda/python:3.11

# Copia los requerimientos y python code
COPY requirements.txt /var/task/
COPY src/ ${LAMBDA_TASK_ROOT} 

# Instala dependencias
RUN pip3 install -r /var/task/requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Define el handler de la Lambda
CMD [ "lambda_function.lambda_handler" ]
