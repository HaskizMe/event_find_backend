# Install dependencies with Conda

```bash
conda env create -f environment.yml
```

# Export dependencies with Conda

```bash
conda env export > environment.yml
```

# Run server locally 

```bash
uvicorn main:app --reload
```