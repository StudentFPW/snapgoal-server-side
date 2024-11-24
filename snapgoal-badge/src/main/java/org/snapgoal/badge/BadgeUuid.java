package org.snapgoal.badge;

public final class BadgeUuid {
    private String uuid;

    public BadgeUuid(String s) { 
        this.uuid = s;
    }

	public String getUuid() {
		return uuid;
	}

	public void setUuid(String uuid) {
		this.uuid = uuid;
	}
}
