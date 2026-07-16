#!/bin/bash

# Configurar descripción, homepage y topics
gh repo edit Kaia-Alenia/nerve-community \
  --description "🧠 Proyectos y retos de código abierto para aprender Python (y más) construyendo herramientas reales con Nerve. Ideal para tu primer PR. 🇲🇽🌎" \
  --homepage "https://github.com/Kaia-Alenia/alenia-nerve" \
  --add-topic python \
  --add-topic hacktoberfest \
  --add-topic good-first-issue \
  --add-topic aprende-python \
  --add-topic comunidad-latam \
  --add-topic open-source \
  --add-topic ipc \
  --add-topic sockets \
  --add-topic beginner-friendly \
  --add-topic spanish \
  --add-topic espanol \
  --add-topic primer-pull-request \
  --add-topic portfolio-projects \
  --add-topic nerve

# Crear o actualizar etiquetas
gh label create "good-first-issue" -c "7057ff" -d "Ideal para tu primer Pull Request" -f
gh label create "nivel-1-principiante" -c "0e8a16" -d "No necesitas experiencia previa" -f
gh label create "nivel-2-intermedio" -c "fbca04" -d "Ya sabes lo básico de Python" -f
gh label create "nivel-3-avanzado" -c "d93f0b" -d "Reto técnico para expertos" -f
gh label create "disponible" -c "c2e0c6" -d "Nadie lo está resolviendo aún" -f
gh label create "en-progreso" -c "fef2c0" -d "Alguien ya lo está resolviendo" -f
gh label create "resuelto" -c "0052cc" -d "Ya tiene un PR aceptado" -f
gh label create "ayuda-buscada" -c "008672" -d "Se busca ayuda extra en este issue" -f
gh label create "documentación" -c "0075ca" -d "Mejoras a los documentos del repo" -f
gh label create "bug" -c "d73a4a" -d "Algo no funciona como debería" -f
gh label create "propuesta-de-reto" -c "a2eeef" -d "Alguien propone un reto nuevo" -f
gh label create "hacktoberfest" -c "ff7518" -d "Cuenta para Hacktoberfest (usar en octubre)" -f
gh label create "primera-vez" -c "c5def5" -d "Contribuyente haciendo su primer PR aquí" -f
gh label create "candidato-a-zenith" -c "ffd700" -d "Contribución destacada, en evaluación para integrarse a zenith-nerve-tools" -f
gh label create "graduado-a-zenith" -c "b60205" -d "Ya se integró oficialmente a zenith-nerve-tools 🎉" -f
