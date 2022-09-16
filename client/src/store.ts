import { User } from './api/models/User';
import { writable, derived } from 'svelte/store';

export const endpoint = writable("")
export const currentUser = writable(new User())