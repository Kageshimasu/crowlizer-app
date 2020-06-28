class InferenceRepositoy:

    @staticmethod
    def get_encoder_path():
        return '../../resources/encoders/target_encoding.pkl'

    @staticmethod
    def get_classifier_paths():
        import glob
        return glob.glob('../../resources/ml_models/classifier/*.pkl')

    @staticmethod
    def get_regressor_paths():
        import glob
        return glob.glob('../../resources/ml_models/regressor/*.pkl')

    @staticmethod
    def get_methods():
        return ['all-in', 'all-or-nothing']
