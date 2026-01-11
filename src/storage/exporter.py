import json
import csv

class ResultsExporter:
    '''Экспорт результатов в различные форматы'''
    
    @staticmethod
    def to_json(analysis_result: dict, output_path: str):
        '''Экспорт в JSON'''
        with open(output_path, 'w') as f:
            json.dump(analysis_result, f, indent=2)
    
    @staticmethod
    def to_csv(analyses: list, output_path: str):
        '''Экспорт в CSV'''
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['File', 'Model', 'Class', 'Probability', 'Time', 'Device'])
            for analysis in analyses:
                writer.writerow(analysis)
