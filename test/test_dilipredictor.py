from dilipred import DILIPRedictor

if __name__ == '__main__':
    smiles = "CCCCCCCO"
    dp = DILIPRedictor(smiles)
    result = dp.predict()
    assert result is not None