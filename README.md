# PiTCT-docs

PiTCT Documents

## Setup Instructions

### GitHub Codespace (Recommended)

1. **Create Codespace**

    Select Create codespace from the `+` button  
    ![codespace](./img/codespace.png)

### Local PC

1. **Install uv**

    [uv](https://docs.astral.sh/uv/getting-started/installation/) is a Python package manager

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Install Dependencies**

    ```bash
    uv sync
    ```

## Edit Documents

### Edit While Previewing Changes

1. **Serve the Documentation Locally**:
    Run the following command to start the live-reloading docs server and see your changes:

    ```bash
    uv run mkdocs serve
    ```

### Adding New Directory

When you add a new directory to the documentation, follow these steps to ensure it is properly integrated and displayed:

1. **Update `.nav.yml`**:
    - Open the `.nav.yml` configuration file.
    - Add an settings for your new directory under the `nav` section

### Reflect Changes on the Production Site

1. **Commit and Push Changes**:
    - Commit your changes to the repository and push them to the remote repository.

    After committing to the main branch, the document site is automatically built and updated using GitHub Actions.
