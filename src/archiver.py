import os, shutil, gzip, datetime

def archive_logs(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.log') or filename.endswith('.txt'):
            file_path = os.path.join(source_dir, filename)
            with open(file_path, 'rb') as f_in:
                with gzip.open(os.path.join(target_dir, filename + '.gz'), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(file_path)
