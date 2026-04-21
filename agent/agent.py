import json
import re

class ReflectionAgent:
    def __init__(self, tree_filepath):
        with open(tree_filepath, 'r') as f:
            data = json.load(f)
        # Convert list of nodes into a dictionary for O(1) lookups
        self.nodes = {node['id']: node for node in data['nodes']}
        self.state_signals = {}
        self.answers = {}

    def interpolate_text(self, text):
        # Finds patterns like {A1_Q1.answer} and replaces them with the actual answer
        matches = re.findall(r'\{([A-Za-z0-9_]+)\.answer\}', text)
        for match in matches:
            if match in self.answers:
                text = text.replace(f"{{{match}.answer}}", self.answers[match])
        return text

    def run(self):
        current_node_id = "start"
        
        print("\n" + "="*50)
        print(" DEEPTHOUGHT DAILY REFLECTION TERMINAL ".center(50))
        print("="*50 + "\n")

        while current_node_id:
            node = self.nodes[current_node_id]
            node_type = node['type']

            if node_type in ['start', 'bridge']:
                print(f"\n{self.interpolate_text(node['text'])}")
                input("\n[Press Enter to continue...]")
                current_node_id = node['next']

            elif node_type == 'question':
                print(f"\nQ: {self.interpolate_text(node['text'])}")
                for idx, option in enumerate(node['options'], 1):
                    print(f"  {idx}. {option['label']}")
                
                choice = 0
                while choice < 1 or choice > len(node['options']):
                    try:
                        choice = int(input("\nSelect an option (number): "))
                    except ValueError:
                        pass
                
                selected_option = node['options'][choice - 1]
                
                # Save answer for interpolation
                self.answers[node['id']] = selected_option['label']
                
                # Tally signals
                signal = selected_option['signal']
                self.state_signals[signal] = self.state_signals.get(signal, 0) + 1
                
                current_node_id = selected_option['next']

            elif node_type == 'decision':
                next_node = node['default']
                # Evaluate conditions deterministically
                for condition in node['conditions']:
                    # Parse condition "signal >= value"
                    parts = condition['if'].split(">=")
                    sig_name = parts[0].strip()
                    threshold = int(parts[1].strip())
                    
                    if self.state_signals.get(sig_name, 0) >= threshold:
                        next_node = condition['next']
                        break
                current_node_id = next_node

            elif node_type == 'reflection':
                print(f"\n--- INSIGHT ---")
                print(self.interpolate_text(node['text']))
                print("---------------")
                input("\n[Press Enter to continue...]")
                current_node_id = node['next']
                
            elif node_type == 'summary':
                print(f"\n=== YOUR DAILY SYNTHESIS ===")
                print(self.interpolate_text(node['text']))
                print("============================\n")
                input("[Press Enter to finish...]")
                current_node_id = node.get('next')

            elif node_type == 'end':
                print(f"\n{node['text']}\n")
                break

if __name__ == "__main__":
    agent = ReflectionAgent('reflection-tree.json')
    agent.run()
