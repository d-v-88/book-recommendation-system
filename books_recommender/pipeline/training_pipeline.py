# Here in pipeline first i need to pass the initial stage so first the data ingestion should be done

from books_recommender.components.stage_00_data_ingestion import DataIngestion

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :returns: none
        """
        self.data_ingestion.initiate_data_ingestion()