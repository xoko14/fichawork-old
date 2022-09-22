<script lang="ts">
    import { ApiClient } from "../../api/apiClient";
    import { token, activeSection } from "../../store";
    import AlertBox from "../components/AlertBox.svelte";
    import { Section } from "../Sections";

    let error: boolean = false
    let username = ""
    let password = ""

    async function login(){
        let usrToken = await ApiClient.logIn(username, password)
        if(usrToken.access_token){
            token.set(usrToken.access_token)
            activeSection.set(Section.CLOCKIN)
        }
        else{
            error = true
        }
    }
</script>

<div class="section">
    <div class="card">
        <p class="m-auto text-3xl mb-4">Log in</p>
        <div class="flex flex-col mb-4">
            <input type="text" placeholder="Username" bind:value={username} class="text-input"/>
            <input type="password" placeholder="Password" bind:value={password} class="text-input"/>
        </div>
        <button on:click={login} class="button">Log in</button>
        {#if error}
            <div class="mt-4">
                <AlertBox message="Incorrect username/password"/>
            </div>
        {/if}
    </div>
</div>
