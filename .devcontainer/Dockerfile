FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9-bullseye

RUN apt-get update && apt-get install --no-install-recommends -y \
    vim

# poetry
USER vscode
RUN curl -sSL https://install.python-poetry.org | python3 -

# shell
RUN echo "set -o vi" >> /home/vscode/.bashrc
RUN echo "bindkey -v" >> /home/vscode/.zshrc