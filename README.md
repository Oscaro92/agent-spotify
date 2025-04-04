# agent-spotify
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=fff)

## 🔧 Installation 

Clone the repository
```shell
git clone https://github.com/oscaro92/agent-spotify.git
cd agent-spotify
```

Create a virtual environment
```shell
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

Install dependencies
```shell
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file with the following variables:
```
OPENAI_API_KEY=sk-...
```

## 🚀 Usage

Run docker 
```shell
docker-compose up -d
```

Stop docker 
```shell
docker-compose down
```

## 📁 Project Structure

```
agent-spotify/
├── agent.py            # Agent
├── app.py              # Chat streamlit
├── .env                # Environment variables
├── README.md           # Documentation
└── requirements.txt    # Dependencies
```

## 📝 License

This project is licensed under the MIT License.