# Django Project Setup and Run Instructions

## Installing Dependencies

1. Ensure you're in the directory containing the `requirements.txt` file.
2. Run the following command to install all required packages:

   ```
   pip install -r requirements.txt
   ```

## Running the Django Server

1. Navigate to your Django project's root directory (where `manage.py` is located):

   ```
   cd test3
   ```

2. Activate venv

   ```
   source venv/bin/activate
   ```

3. Start the Django development server:

   ```
   python manage.py runserver
   ```

   By default, this will start the server on `http://127.0.0.1:8000/`

4. From new terminal navigate to frontend

   ```
   cd test3/app
   ```

5. Install npm packages

   ```
   npm i
   ```

6. Install npm packages

   ```
   npm run serve
   ```

## Accessing Your Django Application

Open a web browser and go to `http://127.0.0.1:8080/`
