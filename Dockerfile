FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# --- Install Node.js for Tailwind ---
ARG NODE_MAJOR=22
RUN apt-get update \
  && apt-get install -y curl gnupg ca-certificates git \
  && mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" > /etc/apt/sources.list.d/nodesource.list \
  && apt-get update && apt-get install -y nodejs \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# --- Set environment variables ---
ENV PYTHONUNBUFFERED=true \
    PATH="/root/.local/bin:${PATH}"

# --- Install Python dependencies ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy the full project ---
COPY . .

# --- Prepare staticfiles directory ---
RUN mkdir -p /app/mysite/staticfiles

# --- Tailwind and collectstatic ---
WORKDIR /app/mysite


RUN python manage.py collectstatic --no-input --verbosity 3

# --- Start the app ---
# CMD ["gunicorn", "mysite.asgi:application", "--bind", "0.0.0.0:8000", "--worker-class", "uvicorn.workers.UvicornWorker", "--timeout", "300"]
