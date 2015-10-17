package models;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by Krishna Ghatia on 10/17/2015.
 */
public class Campaign implements Parcelable {
    private String campId;
    private String campaignUrl;
    private String name;
    private String startDate;
    private String defaultPhoto;
    private String summary;

    public static final Parcelable.Creator<Campaign> CREATOR = new Parcelable.Creator<Campaign>() {
        public Campaign createFromParcel(Parcel p) {
            return new Campaign(p);
        }

        @Override
        public Campaign[] newArray(int i) {
            return new Campaign[0];
        }
    };

    public Campaign(){
        this.campId = "";
        this.name = "";
        this.campaignUrl = "";
        this.defaultPhoto = "";
        this.startDate = "";
        this.summary = "";
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i) {

    }

    public Campaign(Parcel p) {
        campId = p.readString();
        name = p.readString();//p.readTypedList(attenders, Person.CREATOR);
        startDate = p.readString();
        defaultPhoto = p.readString();
        summary = p.readString();

    }

    public Campaign( String campId, String name, String startDate, String campaignUrl, String occupation, String summary) {
        this.campId = campId;
        this.name = name;
        this.startDate = startDate;
        this.campaignUrl = campaignUrl;
        this.defaultPhoto = occupation;
        this.summary = summary;
        //this.creator=creator;
        //this.attenders=attenders;
        // TODO - fill in here, please note you must have more arguments here
    }
}
