#Flowchart of STOFS3D-ATL preprocessing steps

def create_mermaid_flowcharts():
    # Common style definitions
    style = """
classDef scriptClass fill:#5d8aa8,stroke:#333,stroke-width:2px,color:#fff
classDef processClass fill:#98fb98,stroke:#333,stroke-width:2px
classDef fileClass fill:#ffa07a,stroke:#333,stroke-width:2px
"""

    # Flowchart 1: Main Script Flow
    main_flow = "flowchart TD\n" + style + """
    A["jstofs_3d_atl_prep.ecf"]:::scriptClass -->|Calls| B["JSTOFS_3D_ATL_PREP"]:::scriptClass
    B -->|Calls| C["exstofs_3d_atl_prep_processing.sh"]:::scriptClass
    
    A -->|Sets| D[Initial Environment]:::processClass
    B -->|Defines| E[Input/Output Directories]:::processClass
    B -->|Prepares| F[Workspace]:::processClass
    
    D & E & F -.->|Used by| C
"""

    # Flowchart 2: Initial Environment Setup
    env_setup = "flowchart TD\n" + style + """
    D[Initial Environment]:::processClass
    D --> D1[Load Modules]:::processClass
    D --> D2[Set Basic Variables]:::processClass
    D --> D3[Create Working Directory]:::processClass
    D --> D4[Setup Job Logging]:::processClass
    D --> D5[Set Output Control]:::processClass
    D --> D6[Configure Time Settings]:::processClass
    D --> D7[Set Directory Paths]:::processClass
    D --> D8[Set Model Run Parameters]:::processClass
"""

    # Flowchart 3: Output Files Creation
    output_files = "flowchart TD\n" + style + """
    C["exstofs_3d_atl_prep_processing.sh"]:::scriptClass
    C -->|Creates| G[param.nml]:::fileClass
    C -->|Creates| H[bctides.in]:::fileClass
    C -->|Creates| I[River Forcing]:::fileClass
    C -->|Creates| J[Surface Forcing GFS]:::fileClass
    C -->|Creates| K[Surface Forcing HRRR]:::fileClass
    C -->|Creates| L[OBC 3DTH Nudge]:::fileClass
    C -->|Creates| M[Restart File]:::fileClass
"""

    return main_flow, env_setup, output_files

# print out code to separate files
flowcharts = create_mermaid_flowcharts()
flowchart_names = ['main_flow', 'env_setup', 'output_files']

for name, flowchart in zip(flowchart_names, flowcharts):
    with open(f'stofs_flowchart_{name}.mmd', 'w') as f:
        f.write(flowchart)
    print(f"Mermaid flowchart code for {name} has been written to 'stofs_flowchart_{name}.mmd'")
