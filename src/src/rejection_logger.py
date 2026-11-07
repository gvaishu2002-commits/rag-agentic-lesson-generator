class RejectionLogger:

    def log(self, failures):
        with open("rejection_log.txt", "a") as file:
            for failure in failures:
                file.write(failure + "\n")
