//This is an Admin-only fetch wrapper
///it attaches admin tokens, detects expired / invalid tokens
// forces logout on 401

export async function adminFetch(input:RequestInfo, init: RequestInit = {}) {
    const res = await fetch(input, init)
    const token = localStorage.getItem("admin_token")
    
    if(!token)
    {
        //must not be logged in so redirect
        window.location.href = "/#/admin-login"
        throw new Error("Admin not authenticated")
    }
    
    //401 returned when:
    ///- token expired
    ///- token revoked
    ///- token invalid / missing
    if(res.status === 401)
    {
        //clear stale auth state
        localStorage.removeItem("admin_token")
        localStorage.removeItem("admin_role")

        //redirect to login
        window.location.href = "/#/admin-login"

        throw new Error("admin seesion exppired")

    }
    return res
}