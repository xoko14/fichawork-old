import { UserCreate, User } from "./models/User";
import { plainToInstance } from "class-transformer";

export class ApiClient{

    async createUser(userCreate: UserCreate): Promise<User>{
        var response = await fetch("api/users/", {
            method: "POST",
            body: JSON.stringify(userCreate)
        })
        return plainToInstance(User, await response.json())
    }

    async getCurrentUser(): Promise<User>{
        var headers = new Headers()
        headers.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjoxNjYzNDM0ODEzfQ._yvnGR3a3CzeXZ4_ZEKcZK5SWeJsOkSbI0F-0sEDe1U")        
        var response = await fetch("api/users/me",{
            headers: headers
        })
        return plainToInstance(User, await response.json())
    }
}