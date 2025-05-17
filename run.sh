
# Making an venv Envrionment
python3 -m venv venv

# Activating the venv
source venv/bin/activate

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "❌ Virtual Environment is NOT activated."
    echo "👉 Please run : "source venv/bin/activate ". to Activate it First"
    exit 1
fi

echo "✅ Virtual environment is ACTIVATED. Let's gooo! 🚀"

# Installing the requirements
python3 -m pip install -r requirements.txt

# Running the app
python3 main.py