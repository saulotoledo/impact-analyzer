# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-alpine

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Setup PS1 terminal
ENV PS1='\[\033[1;36m\]\u@\h:\w\$\[\033[0m\] '

WORKDIR /workspace

RUN apk add --no-cache git wget jq tree sudo bash bash-completion git-bash-completion colordiff alpine-sdk

# Creates a non-root user with an explicit UID and adds permission to access the /workspace folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /workspace \
    && echo '%wheel ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/wheel && adduser appuser wheel \
    && sed -i 's/\/bin\/ash/\/bin\/bash/g' /etc/passwd \
    && wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh -P /bin \
    && echo "source /bin/git-prompt.sh" >> /etc/bash/bashrc \
    && echo 'export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(__git_ps1 \" (%s)\")\[\033[00m\] $ "' >> /etc/bash/bashrc
USER appuser

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip && python -m pip install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "impact_analyzer.wsgi"]
