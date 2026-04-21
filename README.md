# Daily-reflection-tree
# DT Fellowship Assignment: Daily Reflection Tree

A deterministic, end-of-day reflection tool designed to walk an employee through a structured conversation evaluating their Locus of Control, Orientation, and Radius of Concern.

This project was built as a role-simulation assignment for DeepThought Growth Teams. It demonstrates the ability to translate psychological frameworks into structured, auditable data trees without relying on LLM hallucinations at runtime.

## Repository Structure

* `/tree`: Contains the core data structure (`reflection-tree.json`), a visual Mermaid diagram (`tree-diagram.md`), and the design rationale (`write-up.md`).
* `/agent`: Contains `agent.py`, a lightweight Python CLI engine that deterministically parses the JSON tree, handles user inputs, calculates state signals, and interpolates strings.
* `/transcripts`: Contains sample outputs showing different paths through the tree (e.g., a "Victim/Egocentric" persona vs. a "Victor/Altrocentric" persona).

## How to Read the Tree

The tree is stored as a structured JSON file (`/tree/reflection-tree.json`). 
* **Nodes:** Every interaction is a node. `question` nodes contain fixed options. 
* **Signals:** Options are tagged with signals (e.g., `locus:victor`). 
* **Branching:** `decision` nodes evaluate the accumulated signals deterministically to route the user to the appropriate `reflection` node.
* **Interpolation:** The `summary` node uses string templates (e.g., `{A1_Q1.answer}`) to pull exactly what the user selected during their session.

## How to Run the Agent

The agent is a standard Python script with no external dependencies. 

1. Ensure you have Python installed.
2. Clone or download this repository.
3. Open your terminal and navigate to the root folder of the project.
4. Run the script:
   ```bash
   python agent/agent.py
