def create_mermaid_flowchart():
    mermaid_code = """
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#5d8aa8', 'secondaryColor': '#f0f8ff', 'tertiaryColor': '#f0f8ff' }}}%%

flowchart TD
    classDef scriptClass fill:#5d8aa8,stroke:#333,stroke-width:2px,color:#fff;
    classDef processClass fill:#98fb98,stroke:#333,stroke-width:2px;
    classDef fileClass fill:#ffa07a,stroke:#333,stroke-width:2px;

    A[("jstofs_3d_atl_prep.ecf")]:::scriptClass -->|Calls| B[("JSTOFS_3D_ATL_PREP")]:::scriptClass
    B -->|Calls| C[("exstofs_3d_atl_prep_processing.sh")]:::scriptClass
    
    A -->|Sets| D[Initial Environment]:::processClass
    B -->|Defines| E[Input/Output Directories]:::processClass
    B -->|Prepares| F[Workspace]:::processClass
    
    C -->|Creates| G[param.nml]:::fileClass
    C -->|Creates| H[bctides.in]:::fileClass
    C -->|Creates| I[River Forcing]:::fileClass
    C -->|Creates| J[Surface Forcing GFS]:::fileClass
    C -->|Creates| K[Surface Forcing HRRR]:::fileClass
    C -->|Creates| L[OBC 3DTH Nudge]:::fileClass
    C -->|Creates| M[Restart File]:::fileClass

    D & E & F -.->|Used by| C

    subgraph "Initial Environment Setup"
        D
        D1[Load Modules]:::processClass
        D2[Set Basic Variables]:::processClass
        D3[Create Working Directory]:::processClass
        D4[Setup Job Logging]:::processClass
        D5[Set Output Control]:::processClass
        D6[Configure Time Settings]:::processClass
        D7[Set Directory Paths]:::processClass
        D8[Set Model Run Parameters]:::processClass
        D --> D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8
    end

    subgraph "Output Files"
        G
        H
        I
        J
        K
        L
        M
    end
"""
    return mermaid_code

# Write the Mermaid code to a file
with open('stofs_flowchart.mmd', 'w') as f:
    f.write(create_mermaid_flowchart())

print("Mermaid flowchart code has been written to 'stofs_flowchart.mmd'")
