# Build Frontend Artifacts
FROM node:18.12-alpine AS frontend

CMD ["mkdir", "-p", "/usr/src/limitless/frontend/"]
WORKDIR /usr/src/limitless/frontend/

COPY ["frontend/package.json", "/usr/src/limitless/frontend/"]
RUN npm install && npm cache clean --force

# TODO: Only copy specific resources listed in `tailwind.config.js`
COPY ["apps", "/usr/src/limitless/apps/"]
COPY ["limitless", "/usr/src/limitless/limitless/"]
COPY ["frontend", "/usr/src/limitless/frontend/"]

RUN npm run build-only

# Build Backend Image
FROM python:3.11-slim AS backend

WORKDIR /usr/src/limitless/

# Install System Dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libfreetype6-dev \
    libjpeg-dev \
    libmagic1 \
    libpq-dev \
    libz-dev \
    poppler-utils \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
RUN ["pip", "install", "-U", "pip"]
COPY ["requirements.txt", "./requirements.txt"]
RUN ["pip", "install", "-r", "requirements.txt"]

# Copy Frontend Artifacts
COPY --from=frontend /usr/src/limitless/frontend/dist/ /usr/src/limitless/frontend/dist/

# Copy all project files (filtered by .dockerignore)
COPY [".", "."]

# TODO: Remove editable?
RUN ["pip", "install", "--no-deps", "-e", "."]
