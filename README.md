#ETL Data Pipeline for Sales Data

#About the Project

This project is an ETL (Extract, Transform, Load) Data Pipeline designed to process and load sales data from a CSV file into a MySQL database using Docker & Python. The goal is to automate data ingestion, transformation, and storage.

#📂 Project Structure

ETL-Datapipe/
│── data/                   # Folder for CSV files
│── docker-compose.yml      # Defines MySQL & ETL service
│── Dockerfile              # Build ETL pipeline container
│── requirements.txt        # Python dependencies
│── main.py                 # ETL script
│── db_utils.py             # MySQL connection & table creation
│── README.md               # Documentation

#⚙️ Technologies Used

Python (pandas, mysql-connector-python)

MySQL 8.0 (Database)

Docker & Docker Compose (Containerization)

GitHub (Version Control)

#🛠 Tools Used

VS Code - For development and debugging

Git - Version control

GitHub - Repository hosting

Docker - Containerization of services

MySQL Workbench - Database management and query execution

Bash & Shell Scripting - Automating ETL processes

#🚀 How to Run the Project

1. Clone the Repository

git clone https://github.com/nnnthum/ETL_Datapipeline.git
cd ETL_Datapipeline

2. Run with Docker

docker compose up --build

This will start:
✅ A MySQL container with the database✅ An ETL container that extracts, transforms, and loads data

3. Check the MySQL Database

After the ETL job completes, verify the data:

docker exec -it etl-datapipe-mysql-1 mysql -u user -p

USE sales_db;
SHOW TABLES;
SELECT * FROM sales;

#📈 Expected Output

After running the ETL pipeline, the sales table will be populated with data from sales_data.csv.

#🔥 Future Enhancements

Add Airflow for scheduling ETL jobs

Connect to a Data Warehouse for analytics

Automate data validation before loading

#🤝 Contributing

Pull requests are welcome! Feel free to fork the repository and submit improvements.