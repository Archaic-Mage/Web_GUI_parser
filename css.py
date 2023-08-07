CSS = """
<style>
    .sidebar {
    margin: 0;
    padding: 0;
    width: 200px;
    background-color: #f1f1f1;
    position: fixed;
    height: 100%;
    overflow: auto;
    }

    .sidebar a {
    display: block;
    color: black;
    padding: 16px;
    text-decoration: none;
    }

    .sidebar a.active {
    background-color: #04aa6d;
    color: white;
    }

    .sidebar a:hover:not(.active) {
    background-color: #555;
    color: white;
    }

    div.content {
    margin-left: 200px;
    padding: 1px 16px;
    height: 1000px;
    }
    .text-holder {
        position: relative;
        margin-top: 0.25rem;
        margin-bottom: 0.5rem;
        width: 100%;
        height: 1.5rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    div {
        margin-bottom: 1rem;
    }
    .placeholder {
        color: grey;
    }
    .button {
        position: relative;
        width: 100%;
        margin-top: 0.25rem;
        font-weight: 700;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }
    .input-type {
        font-weight: 700;
        font-size: 1.25rem;
    }
    .add-btn {
        margin-bottom: 0.5rem;
    }
</style>
"""