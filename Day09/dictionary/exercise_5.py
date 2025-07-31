blockfuse_labs = [
        {
            "web2":{"Aaron":50,"Mark":100,"MP":100}, 
            "web3":{"Klo":400, "clark":200, "Lad":320}
        }
    ]
print(blockfuse_labs[0]["web2"])

#using replace or reasign to update
blockfuse_labs[0]["web2"]["Aaron"] += 100
print(blockfuse_labs)
