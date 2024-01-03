import yaml
import os
import glob

directory_path = '_data/exam_qs'
output_html_file = 'topical_exam_resources.html'

unique_topics = set()
unique_difficulties = set()
unique_types = set()

html_content = """---
layout: default
title: Topical Exam Resources
---

<h1>Topical Exam Resources</h1>

<style>
.collapsible {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.collapsible .toggle-icon {
  transition: transform 0.3s ease;
}

.active .toggle-icon {
  transform: rotate(90deg);
}

.active, .collapsible:hover {
  background-color: #ccc;
}

.content {
  display: none;
  overflow: hidden;
  padding: 0 18px;
}
</style>

</head>
<body>
"""

yml_files = glob.glob(os.path.join(directory_path, '*.yml'))

all_topics = {}
topic_order = ['Java', 'Git', 'Testing', 'Lists', 'Linked Lists', 'Arrays', 'Lists', 'Deques', 'Abstraction', 'Inheritance', 'DMS', 'HOFs', 'Generics', 'Exceptions', 'Iterators', 'Comparators', 'Equals', 'Asymptotics', 'Disjoint Sets', 'ADTs', 'BSTs', 'B-Trees', 'Red-Black Trees', 'Hashing', 'Heaps / PQs', 'Tree Traversals', 'Graph Traversals', 'SPTs', 'MSTs', 'Tries', 'Sorting', 'Compression', '2048', 'Percolation', 'Persistence', 'K-D Trees', 'Reductions']

for file_path in yml_files:
    with open(file_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        exam_name = os.path.splitext(os.path.basename(file_path))[0]
        exam_link = data.get('link')

        for question in data['questions']:
            topic = str(question['topic'])
            difficulty = question['difficulty']
            type = question['type']

            unique_topics.add(topic)
            unique_difficulties.add(difficulty)
            unique_types.add(type)
            if topic not in all_topics:
                all_topics[topic] = []
            entry = {
                'exam': exam_name,
                'exam_link': exam_link,
                'difficulty': question['difficulty'],
                'type': question['type'],
                'question_numbers': question['question numbers'],
                'solutions': data['solutions'],
                'walkthrough': data['walkthrough']
            }
            all_topics[topic].append(entry)

def get_custom_sort_key(topic):
    try:
        return topic_order.index(topic)
    except ValueError:
        return float('inf')

topic_options = '\n'.join(f'<option value="{topic}">{topic}</option>' for topic in sorted(unique_topics))
difficulty_options = '\n'.join(f'<option value="{difficulty}">{difficulty}</option>' for difficulty in sorted(unique_difficulties))
type_options = '\n'.join(f'<option value="{type}">{type}</option>' for type in sorted(unique_types))

filter_form_html = "<div class='filter-form'>\n"
filter_form_html += "<label for='topicFilter'>Topic:</label>\n"
filter_form_html += "<select id='topicFilter'>\n<option value=''>All Topics</option>\n{topic_options}\n</select>\n"

filter_form_html += "<label for='difficultyFilter'>Difficulty:</label>\n"
filter_form_html += "<select id='difficultyFilter'>\n<option value=''>All Difficulties</option>\n{difficulty_options}\n</select>\n"

filter_form_html += "<label for='typeFilter'>Type:</label>\n"
filter_form_html += "<select id='typeFilter'>\n<option value=''>All Types</option>\n{type_options}\n</select>\n"

# filter_form_html += "<button onclick='filterQuestions()'>Filter</button>\n"
filter_form_html += "<button id='filterButton' onclick='filterQuestions()'>Filter</button>\n"

filter_form_html += "</div>\n"
filter_form_html += "<p></p>\n"

html_content = html_content + filter_form_html.format(topic_options=topic_options, difficulty_options=difficulty_options, type_options=type_options)

for topic in sorted(all_topics.keys(), key=get_custom_sort_key):
    entries = all_topics[topic]
    topic_id = topic.replace(' ', '-').lower() 
    html_content += f"<button id='{topic_id}-button' class='collapsible'>{topic} <span class='toggle-icon'>&#9656;</span></button>\n" 
    html_content += f"<div id='{topic_id}-content' class='content'>\n<ul>\n"
    for entry in sorted(entries, key=lambda x: x['exam']):
        for q_num in entry['question_numbers']:
            html_content += f"<li data-difficulty='{entry['difficulty']}' data-type='{entry['type']}'>{entry['exam']} &nbsp;"
            html_content += f"<a href='{entry['exam_link']}'>Exam</a> &nbsp;"
            html_content += f"<a href='{entry['solutions']}'>Solution</a> &nbsp;"
            html_content += f"<a href='{entry['walkthrough']}'>Walkthrough</a> &nbsp;"
            html_content += f"Difficulty: {entry['difficulty']} &nbsp;"
            html_content += f"Type: {entry['type']} &nbsp;"
            html_content += f"Question: {q_num}   "  
            html_content += f"<input type='checkbox' id='chk-{entry['exam']}-{q_num}' class='exam-checkbox' />"
            html_content += f"<label for='chk-{entry['exam']}-{q_num}'></label></li>\n"
    html_content += "</ul>\n"
    html_content += "</div>\n\n"


html_content += """
<script>
var coll = document.getElementsByClassName('collapsible');
for (var i = 0; i < coll.length; i++) {
  coll[i].addEventListener('click', function() {
    this.classList.toggle('active');
    var content = this.nextElementSibling;
    content.style.display = content.style.display === 'block' ? 'none' : 'block';
  });
}
</script>

</body>
</html>
"""

with open(output_html_file, 'w') as html_file:
    html_file.write(html_content)

html_content += f"<li data-difficulty='{entry['difficulty']}' data-type='{entry['type']}'>{entry['exam']} &nbsp;"
html_content += """
<script>
function filterQuestions() {
    var topicFilter = document.getElementById('topicFilter').value;
    var difficultyFilter = document.getElementById('difficultyFilter').value;
    var typeFilter = document.getElementById('typeFilter').value;

    var coll = document.getElementsByClassName('collapsible');
    for (var i = 0; i < coll.length; i++) {
        var content = coll[i].nextElementSibling;
        var listItems = content.getElementsByTagName('li');
        var topicMatch = false;

        var topic = coll[i].id.replace('-button', '').replace(/-/g, ' ').toLowerCase();

        if (!topicFilter || topic.toLowerCase() === topicFilter.toLowerCase()) {
            topicMatch = true; 
        }

        for (var j = 0; j < listItems.length; j++) {
            var item = listItems[j];
            var difficultyMatch = !difficultyFilter || item.getAttribute('data-difficulty') === difficultyFilter;
            var typeMatch = !typeFilter || item.getAttribute('data-type') === typeFilter;
            
            item.style.display = (topicMatch && difficultyMatch && typeMatch) ? '' : 'none';
        }

        var anyVisible = Array.from(listItems).some(function(item) {
            return item.style.display !== 'none';
        });

        coll[i].style.display = anyVisible ? '' : 'none';
        content.style.display = anyVisible && coll[i].classList.contains('active') ? 'block' : 'none';
    }
}

document.getElementById('filterButton').onclick = filterQuestions;
</script>
"""


html_content += "</body>\n</html>"

checkbox_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var checkboxes = document.querySelectorAll('.exam-checkbox');
    checkboxes.forEach(function(checkbox) {
        var isChecked = localStorage.getItem(checkbox.id) === 'true';
        checkbox.checked = isChecked;

        checkbox.addEventListener('change', function() {
            localStorage.setItem(checkbox.id, checkbox.checked);
        });
    });
});
</script>
"""

html_content += checkbox_script

with open(output_html_file, 'w') as html_file:
    html_file.write(html_content)