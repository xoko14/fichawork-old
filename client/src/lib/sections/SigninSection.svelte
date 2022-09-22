<script lang="ts">
    import { ApiClient } from "../../api/apiClient";
    import { User, UserCreate } from "../../api/models/User";
    import AlertBox from "../components/AlertBox.svelte";
    //import {bcrypt} from 'bcrypt'


    let username: string
    let name: string
    let password: string
    let rPassword: string

    let error: boolean = false;
    let errorMessage: string
    let verified: boolean = false

    function verifyUsername(): boolean{
        if(!/^[\w\d\-_]{1,25}$/.test(username?? "")){
            errorMessage = "Username must have between 1 and 10 characters and only contain letters, numbers, <code>-</code> or <code>_</code>."
            return false
        }
        return true
    }

    function verifyName(): boolean{
        if(!/.{1,100}/.test(name?? "")){
            errorMessage = "Name must be between 1 and 100 characters."
            return false
        }
        return true
    }

    function verifyPassword(): boolean{
        if(!/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}\[\]:;<>,.?\/~_+-=|\\]).{8,32}$/.test(password?? "")){
            errorMessage = "Password must be between 8 and 32 characters and inlude at least one uppercase, lowercase, number and special character."
            return false
        }
        if(password != rPassword){
            errorMessage = "Passwords must match."
            return false
        }
        return true
    }

    function verify(){
        if(!verifyUsername()) {error = true; console.log("failed username"); return}
        if(!verifyName()) {error = true; return}
        if(!verifyPassword()) {error = true; return}
        error = false
        verified = true
    }

    async function signin(){
        verify()
        if(!verified) return
        let user = new UserCreate();
        user.name = name
        user.password = password//bcrypt.hashSync(password, 12);
        user.username = username
        ApiClient.createUser(user).then(user => {
            if (user.name == null){
                errorMessage = "Error creating account."
                error = true
            }
        })
    }
    
</script>

<div class="section">
    <div class="card">
        <p class="m-auto text-3xl mb-4">Sign in</p>
        <div class="flex flex-col mb-4">
            <input type="text" placeholder="Username" bind:value={username} class="text-input"/>
            <input type="text" placeholder="Name" bind:value={name} class="text-input"/>
            <input type="password" placeholder="Password" bind:value={password} class="text-input"/>
            <input type="password" placeholder="Repeat password" bind:value={rPassword} class="text-input"/>
        </div>
        <button on:click={signin} class="button">Sign in</button>
        {#if error}
            <div class="mt-4">
                <AlertBox message={errorMessage}/>
            </div>
        {/if}
    </div>
</div>