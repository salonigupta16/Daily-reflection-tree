# Daily Reflection Tree Architecture

```mermaid
graph TD
    START((Start)) --> A1_Q1[A1_Q1: Setback Narrative]
    A1_Q1 --> A1_Q2[A1_Q2: Task Completion]
    A1_Q2 --> A1_Q3[A1_Q3: Unplanned Changes]
    
    A1_Q3 --> A1_DECISION{Locus Decision}
    A1_DECISION -->|Victor >= 2| A1_REFLECT_VICTOR[Victor Reflection]
    A1_DECISION -->|Victim >= 2| A1_REFLECT_VICTIM[Victim Reflection]
    
    A1_REFLECT_VICTOR --> BRIDGE_1_2((Bridge 1-2))
    A1_REFLECT_VICTIM --> BRIDGE_1_2
    
    BRIDGE_1_2 --> A2_Q1[A2_Q1: Workplace Expectations]
    A2_Q1 --> A2_Q2[A2_Q2: Colleague Interactions]
    A2_Q2 --> A2_Q3[A2_Q3: Job Description]
    
    A2_Q3 --> A2_DECISION{Orientation Decision}
    A2_DECISION -->|Contribution >= 2| A2_REFLECT_CONTRIB[Contribution Reflection]
    A2_DECISION -->|Entitled >= 2| A2_REFLECT_ENTITLE[Entitled Reflection]
    
    A2_REFLECT_CONTRIB --> BRIDGE_2_3((Bridge 2-3))
    A2_REFLECT_ENTITLE --> BRIDGE_2_3
    
    BRIDGE_2_3 --> A3_Q1[A3_Q1: Difficult Decisions]
    A3_Q1 --> A3_Q2[A3_Q2: Success Metric]
    A3_Q2 --> A3_Q3[A3_Q3: Colleague Friction]
    
    A3_Q3 --> A3_DECISION{Radius Decision}
    A3_DECISION -->|Altrocentric >= 2| A3_REFLECT_ALTRO[Altrocentric Reflection]
    A3_DECISION -->|Egocentric >= 2| A3_REFLECT_EGO[Egocentric Reflection]
    
    A3_REFLECT_ALTRO --> PRE_SUMMARY((Pre-Summary Bridge))
    A3_REFLECT_EGO --> PRE_SUMMARY
    
    PRE_SUMMARY --> SUMMARY[Final Summary & Interpolation]
    SUMMARY --> END((End Session))
