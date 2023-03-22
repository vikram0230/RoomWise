# RoomWise

RoomWise is a highly scalable and intelligent room reservation system that leverages the power of Machine Learning (ML) to prioritize customers and predict cancellations with 90% accuracy. It is designed and developed using Flutter, MongoDB, and FastAPI, and utilizes open hotel data to power the ML pipeline that drives the system's priority queue.

The system provides a seamless room reservation experience to customers with the ability to book the available rooms and assists hotel managers manage all their reservations in one place. The ML models integrated into the system help to optimize profits by prioritizing customers based on factors such as their past booking history and predicted likelihood of cancellation.

## Features

- Seamless room reservation experience for customers
- ML models for prioritizing customers and predicting cancellations with 90% accuracy
- Open hotel data used to power the ML pipeline
- Containerized API and database using Docker for scalability and portability
- Deployed on AWS for high availability and scalability

## How it Works

The Customer Analysis System is designed to process and store data from a customer booking portal. Data is collected and stored in MongoDB using FastAPI, and can be queried as required.

The system also includes built-in machine learning models for prioritising customers and predicting cancellations. These models include Support Vector Machines for predicting cancellations and Random Forest for prioritising customers to achieve a high level of accuracy.

Finally, the Customer Analysis System provides managers with the ability to analyse trends in customer behaviour, identify potential areas for improvement, and create data-driven mitigation plans to reduce cancellations and improve profitability.

## Technologies Used

- Flutter - Cross-platform mobile app development framework
- MongoDB - Document-oriented NoSQL database
- FastAPI - Web framework for building APIs with Python 3.6+ based on standard Python type hints
- Docker - Platform for building, shipping, and running applications in containers
- AWS - Cloud computing platform for deploying and scaling web applications

## Installation and Setup

1. Clone the repository to your local machine.
2. Install Docker and Docker Compose.
3. Navigate to the root directory of the project and run the following command to start the system:

    ```powershell
    docker-compose up
    ```

4. Access the system by opening the following URL in your web browser:

    ```powershell
    http://localhost:8080/
    ```