def tsv_to_yaml(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()


    data_lines = lines[2:]  

    yaml_lines = ["questions:"]

    for line in data_lines:
        columns = line.strip().split('\t')

        question_number = columns[0].strip() if len(columns) > 0 else ''
        question_name = columns[1].strip() if len(columns) > 1 else ''
        question_type = columns[3].strip() if len(columns) > 3 else ''
        difficulty = columns[4].strip() if len(columns) > 4 else ''

   
        topics = columns[5:]

       
        topics = [topic.strip() for topic in topics if topic.strip()]

        for topic in topics:
            yaml_lines.append("  - topic: " + topic)
            yaml_lines.append("    difficulty: " + difficulty)
            yaml_lines.append("    type: " + question_type)
            yaml_lines.append("    question numbers:")
            yaml_lines.append("      - " + question_number)

    with open(output_file, 'w') as file:
        file.write("\n".join(yaml_lines))

tsv_to_yaml("exam_tsv/EXAM", "_data/exam_qs/EXAM")
