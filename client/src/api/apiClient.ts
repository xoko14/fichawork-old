import { UserCreate, User } from "./models/User";
import { plainToInstance } from "class-transformer";

export class ApiClient{
    private ENDPOINT: string

    constructor(endpoint: string){
        this.ENDPOINT = endpoint
    }

    async createUser(userCreate: UserCreate): Promise<User>{
        var response = await fetch(this.ENDPOINT+"api/users/", {
            method: "POST",
            body: JSON.stringify(userCreate)
        })
        return plainToInstance(User, await response.json())
    }

    async getCurrentUser(): Promise<User>{
        var headers = new Headers()
        headers.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjoxNjYyODkyNTU2fQ.5J7Cb2z8KBVDdBtgroe4SW5ssonr-F_fqaLwcmmCsP8")
        var response = await fetch(this.ENDPOINT+"api/users/me/",{
            headers: headers
        })
        return plainToInstance(User, await response.json())
    }
}