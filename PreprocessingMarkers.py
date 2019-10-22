class PreprocessingMarkers:
    def __init__(self):
        self.all_true = False
        self.markers = {'qualitative_marker': False, 'null_marker': False, 'outlier_marker': False,
                        'separate_marker': False, 'target_marker': False, 'standardize_marker': False,
                        'cluster_marker': False, 'processed_marker': False, 'processed_finalized': True}

    def get_all_markers(self):
        if self.all_true is True:
            return True
        else:
            if self.markers['qualitative_marker'] and self.markers['null_marker']\
                    and self.markers['outlier_marker'] and self.markers['separate_marker'] \
                    and self.markers['target_marker'] and self.markers['standardize_marker']\
                    and self.markers['cluster_marker'] is True:
                self.all_true = True
                return True
            else:
                return False

    def get_markers(self):
        return self.markers

    def set_processed_finalized(self):
        self.markers['processed_finalized'] = False

    def get_processed_finalized(self):
        return self.markers['processed_finalized']

    def set_processed_marker(self):
        self.markers['processed_marker'] = True

    def get_processed_marker(self):
        return self.markers['processed_marker']

    def set_qualitative_marker(self):
        self.markers['qualitative_marker'] = True

    def get_qualitative_marker(self):
        return self.markers['qualitative_marker']

    def set_null_marker(self):
        self.markers['null_marker'] = True

    def get_null_marker(self):
        return self.markers['null_marker']

    def set_outlier_marker(self):
        self.markers['outlier_marker'] = True

    def get_outlier_marker(self):
        return self.markers['outlier_marker']

    def set_target_marker(self):
        self.markers['target_marker'] = True

    def get_targer_marker(self):
        return self.markers['target_marker']

    def set_separate_marker(self):
        self.markers['separate_marker'] = True

    def get_separate_marker(self):
        return self.markers['separate_marker']

    def set_standardize_marker(self):
        self.markers['standardize_marker'] = True

    def get_standardize_marker(self):
        return self.markers['standardize_marker']

    def set_cluster_marker(self):
        self.markers['cluster_marker'] = True

    def get_cluster_marker(self):
        return self.markers['cluster_marker']