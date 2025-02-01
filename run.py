from app import app, db


if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Tables created successfully")
        except Exception as e:
            print(f"Error creating tables: {e}")
            
    app.run(debug=True, port='5050')