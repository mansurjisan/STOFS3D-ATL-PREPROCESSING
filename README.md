# STOFS3D-ATL-PREPROCESSING

This repository contains the description and workflow visuals associated with STOFS 3D Atlantic (STOFS3D-ATL) model.

## Overview

The preprocessing workflow for STOFS3D-ATL involves several scripts that work together to set up the model environment, prepare input data, and create necessary configuration files. This README provides an overview of the script hierarchy and workflow through a table and several flowcharts.

## Script Hierarchy

The following table outlines the main scripts involved in the preprocessing stage and their purposes:

| Main Script | Scripts Called | Purpose |
|-------------|----------------|---------|
| jstofs_3d_atl_prep.ecf | JSTOFS_3D_ATL_PREP | Initiates the preparation process |
| JSTOFS_3D_ATL_PREP | 1. exstofs_3d_atl_prep_processing.sh<br>2. setpdy.sh | 1. Executes the main preparation tasks<br>2. Sets up date variables |
| exstofs_3d_atl_prep_processing.sh | 1. stofs_3d_atl_create_param_nml.sh<br>2. stofs_3d_atl_create_bctides_in.sh<br>3. stofs_3d_atl_create_river_forcing_nwm.sh<br>4. stofs_3d_atl_create_surface_forcing_gfs.sh<br>5. stofs_3d_atl_create_surface_forcing_hrrr.sh<br>6. stofs_3d_atl_create_obc_3dth_nudge.sh<br>7. stofs_3d_atl_create_river_st_lawrence.sh<br>8. stofs_3d_atl_create_obc_3d_th.sh | 1. Creates param.nml file<br>2. Creates bctides.in file<br>3. Creates river forcing from NWM<br>4. Creates surface forcing from GFS<br>5. Creates surface forcing from HRRR<br>6. Creates OBC 3DTH nudging<br>7. Creates forcing files for the St. Lawrence River<br>8. Creates 3D temperature and salinity files |

## Workflow Flowcharts

The preprocessing workflow is visualized through several flowcharts, each focusing on a specific aspect of the process. Click on the links below to view the interactive flowcharts:

1. [Main Components](https://mermaid.live/view#pako:eNqFkl1r2zAUhv-KUGBXjmtHju3oYtDGCWwMGpaMwuJhVPso0apIRpLXZGn--5Q2A0NGJxA6L5znPR_oiGvdAKaYS_1cb5lxaFWUqlS1ZNYWwJGtjWjd9CwRF1LSwbjJGcsD64x-AjoghFzi4bNo3JaO2n1Qa6kNHXDOe1at0TVY2_ea5Pxx8r5Xz8Az0Kc5Z1HG_kOXCvlzuy7xT-s0txVpKuZk1RpoQ6h5iX9QSvtjDocfX6ZMSvuC7jz2ebm6ny8rUlS3qy_V4utscYW81bjrk1NPwv6qYnVZglCb0G7_YXRp99VqCc47FetPSjjBJJqpX8JotQPlzlx_n_0O_KqEAk_OPNl27ua-c_5BhTBQO20E2PfwhW-TmTM_Xz9o82RbVsM18IYU6AOa-TtHw9Cz3yw06PHgxy8VDvAOzI6Jxv-v4zm9xG4LOygx9WEDnHXSlbhUJ5_KOqeXB1Vj6kwHATa622wx5Uxar7q2YQ4KwTaG7f6mtEx917ovMT3iPabJZBLmUUaSNJ-MSBaTAB8wjUkSknGap9loRNKIxKcA_37lozCNkyxOkyhLoigbJ-T0B0KfB8Y)
   - Overview of the main preprocessing components and their interactions.

2. [Initial Environment Setup](https://mermaid.live/view#pako:eNqFk8tu2zAQRX-FoLdyoIdliVx0UauLFglaNEEL1OpiLA0lIhQpUGQT1_C_h3bTQotC4WoGuOfOA5wTbUyLlFOhzFPTg3Xkoap1rRsF01ShIFNj5eh2l5QIqRRf5W0JUEaTs-YR-SrLstd4_SRb1_N0fI4ao4zlKyHEzGq0psFpmnuxUhzYstfMIDA4p4WAuIA36FqT8Kr9Ry2dBEU-6F_SGj2gdj855_OmXqVkvX5HqmR_a6Ald6b1CqdFabq_R0fewyQb8g2shMNbRLbfWQSH5Luxj1J3pJIWG2fscRHbXAr5kXwyB3Jrui6Qi_r82thn70bvyM7osBy1CGz3QSVk5y2SBzkgCbwLVZanKa5l_o1AvoDrl4nySoTdoiJfvQ6EhQEd2v9gNKID2gFkG_7p6WJTU9fjgDXlIWxRgFeuprU-Byl4Z-6PuqHcWY8RtcZ3PeUC1BQyP7Zh65WELtT7KxlB_zBmnlJ-os-Ul_FNzIptxoqM5VmcpBE9Up7F2U0ex8mGJemWlZvyHNHfVz4J8nyTFqxkLGdFsi0jiq0MO7n7c2XXYzu_AA0pIxw)
   - Details of the initial environment setup process.

3. [Workspace Preparation](https://mermaid.live/view#pako:eNqVVe9v2jAQ_Vcs9yt05EcD8aRJJSndJBgVUFVa2Ac3OcBqiCPHWctQ__c5dugyBGmXTzn5vXfnu5fLHsc8AUzwWtB8gxbhMkPqiVNaFCGsUC54DEURVDFasTQlF_5g9egPOoUU_AnIheM49Xv3mSVyQ-z85fORSkIlbUoM-sHN6Pq_JIpYsFw2RUaj617_XREjcx09cPFU5DQGdCcgp4JKxrOfhJDmDQ14GAUCqAQUMgGx5GKH5lKUsSwFnGYEUcDz3acxy54UVEnHaMRSKE6jw2gOEt3n6FuWlxKFqjlozGNd0RnKTWSqBjQtpSbVpbFTSeo7o273Cxo2g6AZhM3g5sAaGpZ16MGEsgzNyuxvM840zfDsA29ePiZtNWqOXZOsSLBfICrUm1WOIHa0XhVtACfaCNEq4UZC8naRq0hAIamQR6B6zKaJVqQHfStY0jbmGm0b9JCXWUKVlQKeJawa9Qe4juHeKbtuQYJAC9jmqWrv2aGHZrSWttjtaG7cdUfl5owXDd7W-K-z2eyDBEcTZovph1O4mvH9YdKGr91uLPnmwWA6md4v3nNgzXpz4AxEu20NrSgfze5b4jGsIUuW2BxUz9hSH57mnM6pMXakb_RPpiODaZzqmV5i1XljnRlElVhVhDt4C2JLWaJ28r46WmK5gS0sMVGvCaxomcqqxFcFpaXk810WY6L2E3Sw4OV6g8mKpoWKylxVASGj6n7bAySn2Q_OmyEme_yCSdeynUu_7_d6juU5fcd1Bh28w8Rxry77ru_bV5ZjW57nvXbwb61gXfZ8z-3Znut6g55n2x0MytpcTMwvRf9ZXv8AchEIdw)
   - Flowchart illustrating the workspace preparation process.

4. [Pre-processing Steps](https://mermaid.live/view#pako:eNqFkk2PmzAQhv-KNbkSlPARjA89NFE2_ZbIngpV5DXjgAoY2aabbTb_fZ0qW6G2Kj7NSM_zeizPGYQqERjIRj2KimtL7jdFV3Si4cZsUBIjdN3b9bUlsm4aNotLyjn1jNXqO7JZGIa3ev5Yl7ZiQX_yhGqUZjMp5Siq10qgMeOslMqH9P9ZowDn4NiWki8SPmEXHXFnnReAJ2OVNIewPHDbHHqN_eE2U90dfVMV8I0xNnrxzSXz-ZvntUZu0TyTu7znmrd-1zZX_PdQ_4R3-YOwdYnGr7tp-l2e1T9Qk63Swo00LbzP94OWXOCrQu62-2ntw1_aLsuyae9j_uXtmoSb-x35PJRHnDY-5Rkae92rreP-4MGDFnXL69Jt4PnqF2ArbLEA5soSJR8aW0DRXRzKB6v2T50AZvWAHmg1HCtgkjfGdUNfuhs3NT-6v3lFet59VWrcAjvDCVji08UyoWlMY5qu4njpwROwIIz81SpOwyBMIkqDJLp48PNXwNJfLKMojcMkSJIgWK7o5QW1ahG-
)
   - Detailed flowchart of the pre-processing steps.

These flowcharts provide a visual representation of the various stages and components involved in the STOFS3D-ATL preprocessing workflow.

## Usage

To use these preprocessing scripts:

1. Ensure you have the necessary permissions and access to the required data sources.
2. Follow the script hierarchy as outlined in the table above.
3. Run the scripts in the order specified, starting with `jstofs_3d_atl_prep.ecf`.

For more detailed instructions on running each script, please refer to the individual script documentation or comments within the code.

## Contributing

If you wish to contribute to this preprocessing workflow or have suggestions for improvements, please open an issue or submit a pull request.

## License

[Insert appropriate license information here]
