import os
from collections import Counter

def get_top_terms(folder_path):
    all_terms = []

    for (root,dirs,files) in os.walk('folder_path', topdown=True):
        print(folder_path)
        for file in files:
            print(file)
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as file:
                    terms = file.read().strip().split(',')
                    all_terms.extend(terms)

    term_counts = Counter(all_terms)
    top_terms = term_counts.most_common(10)

    return top_terms

folder_path = 'E:\git_projx\kohya_ss\aa_train_test_utils\Test\image\50_test'

if not os.path.isabs(folder_path):
    folder_path = os.path.abspath(folder_path)

print("started")
top_terms = get_top_terms(folder_path)

print('Top 10 terms with highest frequency:')
for term, count in top_terms:
    print(f'Term: {term.strip()}, Count: {count}')
