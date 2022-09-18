<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import { Section } from "./lib/Sections";
  import AboutSection from "./lib/sections/AboutSection.svelte";
  import AccountSection from "./lib/sections/AccountSection.svelte";
  import ClockInSection from "./lib/sections/ClockInSection.svelte";
  import ExportSection from "./lib/sections/ExportSection.svelte";
  import HistorySection from "./lib/sections/HistorySection.svelte";
  import Sidebar from "./lib/sidebar/Sidebar.svelte";
  import {activeSection} from "./store"
</script>

<main>
  <div class="flex transition-all">
    <Sidebar/>
    {#if $activeSection == Section.CLOCKIN}
      <ClockInSection />
    {:else if $activeSection == Section.HISTORY}
      <HistorySection />
    {:else if $activeSection == Section.ACCOUNT}
      <AccountSection />
    {:else if $activeSection == Section.EXPORT}
      <ExportSection />
    {:else if $activeSection == Section.ABOUT}
      <AboutSection />
    {/if}
  </div>
</main>

<style>
</style>
