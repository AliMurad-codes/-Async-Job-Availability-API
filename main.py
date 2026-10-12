import asyncio
import time

from fastapi import FastAPI


# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Async Engineer Availability API",
    description="A beginner-friendly FastAPI project demonstrating async/await.",
    version="1.0.0",
)


# --------------------------------------------------
# Fake external API
# --------------------------------------------------

async def get_engineer(engineer_id: int):
    """
    Pretend that we are calling an external API
    to get information about one engineer.
    """

    print(f"Starting request for Engineer {engineer_id}")

    # Pretend the external API takes 1 second
    await asyncio.sleep(1)

    print(f"Finished request for Engineer {engineer_id}")

    return {
        "engineer_id": engineer_id,
        "name": f"Engineer {engineer_id}",
        "available": True,
    }


# --------------------------------------------------
# Async endpoint
# --------------------------------------------------

@app.get("/engineers/availability")
async def check_engineers_availability():
    """
    Check availability of 10 engineers concurrently.
    """

    # Start timer
    start_time = time.perf_counter()

    print("\nChecking engineer availability...\n")

    # Create 10 async tasks
    tasks = [
        get_engineer(engineer_id)
        for engineer_id in range(1, 11)
    ]

    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)

    # Stop timer
    end_time = time.perf_counter()

    # Calculate execution time
    execution_time = end_time - start_time

    print("\nAll engineers checked.")
    print(f"Execution time: {execution_time:.2f} seconds\n")

    # Return API response
    return {
        "message": "Engineer availability checked successfully",
        "total_engineers": len(results),
        "execution_time_seconds": round(execution_time, 2),
        "engineers": results,
    }


# --------------------------------------------------
# Simple health-check endpoint
# --------------------------------------------------

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }