Como estoy corriendo versiones differentes de python y docker gracias al proyecto final todo se despelota y es duro trabajar en otros proyectos. Deberia funcionar pero se bugea por ser una version 2.1+ mas.

e-commerce-chat-ai/
│
├── src/
│   ├── domain/            # Entidades y lógica del dominio
│   ├── application/       # Casos de uso y servicios
│   └── infrastructure/    # API, DB y proveedores IA
│
├── tests/                 # Pruebas unitarias
├── Dockerfile             # Imagen Docker
├── docker-compose.yml     # Orquestación
├── requirements.txt       # Dependencias
├── .env.example           # Variables de entorno de ejemplo
└── README.md

Instalación y ejecución local
git clone https://github.com/Ssanchezl3/TallerZapatos.git
cd TallerZapatos

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
uvicorn src.infrastructure.api.main:app --reload

