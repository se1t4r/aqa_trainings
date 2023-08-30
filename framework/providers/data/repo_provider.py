class RepositoryProvider:

    @staticmethod
    def existing_repo():
        return {
            "name": 'aqa_trainings',
            "total_count": 1
        }
    
    @staticmethod
    def non_existing_repo():
        return {
            "name": 'alksjfalkwjelkj21',
            "total_count": 0
        }