FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY ${PWD}/code/main.py ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from project folder.

COPY ${PWD}/requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "main.handler" ]
