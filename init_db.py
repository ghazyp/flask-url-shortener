from app import db, app

# Ensure we are inside the Flask application context
with app.app_context():
    db.create_all()
    print("✅ Database has been successfully created!")
